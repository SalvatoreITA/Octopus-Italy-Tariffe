"""Gestore dell'aggiornamento dati da Octopus Energy."""
import logging
import json
import re
from datetime import timedelta
import aiohttp

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, URL

_LOGGER = logging.getLogger(__name__)

class OctopusTariffeCoordinator(DataUpdateCoordinator):
    """Classe per gestire lo scraping dal sito Octopus."""

    def __init__(self, hass):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(hours=12),
        )

    async def _async_update_data(self):
        """Scarica l'HTML e lo processa estraendo il JSON nascosto."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(URL, headers={"User-Agent": "Mozilla/5.0"}) as response:
                    response.raise_for_status()
                    html = await response.text()
                    return self._parse_html(html)
        except Exception as err:
            raise UpdateFailed(f"Errore di connessione a Octopus: {err}")

    def _parse_html(self, html):
        """Estrae i prezzi dal blocco JSON nascosto nella pagina."""
        data = {}

        try:
            # Troviamo il blocco JSON nascosto nel tag script __NEXT_DATA__
            json_match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
            if not json_match:
                _LOGGER.error("Blocco dati JSON non trovato nella pagina.")
                return data

            # Carichiamo il JSON
            json_str = json_match.group(1)
            site_data = json.loads(json_str)

            # Navighiamo nella lista dei prodotti
            products = site_data.get("props", {}).get("pageProps", {}).get("products", [])

            for prod in products:
                name = prod.get("fullName", "").lower()
                params = prod.get("params", {})

                # Estraiamo i numeri puri e crudi (Quota Fissa e Materia Prima)
                try:
                    standing_charge = float(str(params.get("annualStandingCharge", "0")).replace(',', '.'))
                    consumption_charge = float(str(params.get("consumptionCharge", "0")).replace(',', '.'))
                except ValueError:
                    continue

                # Assegnazione blindata
                if "fissa 12m" in name and "gas" not in name:
                    data["fissa_luce"] = standing_charge
                    data["fissa_12m_luce"] = consumption_charge
                elif "fissa 12m gas" in name:
                    data["fissa_gas"] = standing_charge
                    data["fissa_12m_gas"] = consumption_charge
                elif "flex mono" in name:
                    data["flex_luce"] = standing_charge
                    data["flex_mono_luce"] = consumption_charge
                elif "flex multi" in name:
                    data["flex_multi_luce"] = consumption_charge
                elif "flex gas" in name:
                    data["flex_gas"] = standing_charge
                    data["flex_gas_materia"] = consumption_charge

        except Exception as e:
            _LOGGER.error(f"Errore durante il parsing del JSON Octopus: {e}")

        return data
