"""Piattaforma Sensori per Octopus Tariffe."""
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Aggiunge i sensori in base alla configurazione UI."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    sensors = [
        # --- COSTI FISSI (PCV / QVD) ---
        OctopusTariffaSensor(coordinator, "Octopus Fissa Commercializzazione Luce", "fissa_luce", "€/anno"),
        OctopusTariffaSensor(coordinator, "Octopus Fissa Commercializzazione Gas", "fissa_gas", "€/anno"),
        OctopusTariffaSensor(coordinator, "Octopus Variabile Commercializzazione Luce", "flex_luce", "€/anno"),
        OctopusTariffaSensor(coordinator, "Octopus Variabile Commercializzazione Gas", "flex_gas", "€/anno"),

        # --- MATERIA PRIMA (Energia / Gas) ---
        OctopusTariffaSensor(coordinator, "Octopus Fissa 12M Luce", "fissa_12m_luce", "€/kWh"),
        OctopusTariffaSensor(coordinator, "Octopus Fissa 12M Gas", "fissa_12m_gas", "€/Smc"),
        OctopusTariffaSensor(coordinator, "Octopus Flex Gas", "flex_gas_materia", "€/Smc"),
        OctopusTariffaSensor(coordinator, "Octopus Flex Mono Luce", "flex_mono_luce", "€/kWh"),
        OctopusTariffaSensor(coordinator, "Octopus Flex Multi Luce", "flex_multi_luce", "€/kWh"),
    ]

    async_add_entities(sensors)

class OctopusTariffaSensor(CoordinatorEntity, SensorEntity):
    """Rappresentazione di un sensore Octopus."""

    def __init__(self, coordinator, name, key, unit):
        """Inizializza il sensore."""
        super().__init__(coordinator)
        self._name = name
        self._key = key
        self._attr_unique_id = f"octopus_tariffe_{key}"
        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_icon = "mdi:lightning-bolt" if "luce" in key.lower() else "mdi:fire"
        if "commercializzazione" in name.lower():
            self._attr_icon = "mdi:cash-multiple"
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self):
        """Restituisce lo stato del sensore."""
        if self.coordinator.data and self._key in self.coordinator.data:
            val = self.coordinator.data[self._key]
            if self._attr_native_unit_of_measurement == "€/anno":
                return round(val, 2)
            return round(val, 5)
        return None
