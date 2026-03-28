"""Config flow per Octopus Tariffe."""
import logging
from homeassistant import config_entries
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class DomHouseOctopusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestisce il processo di configurazione via interfaccia grafica."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Gestisce il primo passaggio dell'installazione."""
        # Controlla se l'integrazione è già stata installata
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        # Se l'utente clicca su 'Invia', crea l'integrazione
        if user_input is not None:
            return self.async_create_entry(title="Octopus Tariffe", data={})

        # Mostra la maschera di conferma
        return self.async_show_form(step_id="user")
