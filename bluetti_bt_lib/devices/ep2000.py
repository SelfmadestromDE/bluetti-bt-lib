class EP2000(BaseDeviceV2):
    def __init__(self):
        super().__init__(
            [
                # --- BATTERIE DATEN (Register 100+) ---
                UIntField(FieldName.BATTERY_SOC, 102),               # Hex 0x43 gefunden
                DecimalField(FieldName.BATTERY_VOLTAGE, 103, 1),     # Batteriespannung
                DecimalField(FieldName.BATTERY_CURRENT, 104, 1),     # Batteriestrom (A)
                IntField(FieldName.BATTERY_POWER, 105),              # Batterie Leistung (W)
                
                # --- PV EINGANG (Register 1200+) ---
                # String 1
                UIntField(FieldName.PV_S1_POWER, 1212),              # Dein Wert 0x0514 -> 1300W
                DecimalField(FieldName.PV_S1_VOLTAGE, 1213, 1),
                DecimalField(FieldName.PV_S1_CURRENT, 1214, 1),
                # String 2
                UIntField(FieldName.PV_S2_POWER, 1220),
                DecimalField(FieldName.PV_S2_VOLTAGE, 1221, 1),
                DecimalField(FieldName.PV_S2_CURRENT, 1222, 1),

                # --- NETZ / GRID (Register 1300+) ---
                DecimalField(FieldName.GRID_FREQUENCY, 1300, 1),
                DecimalField(FieldName.GRID_P1_VOLTAGE, 1314, 1),    # Phase 1 Spannung
                IntField(FieldName.GRID_P1_POWER, 1315),             # Dein Wert 0x015E -> ~350W
                DecimalField(FieldName.GRID_P2_VOLTAGE, 1320, 1),
                IntField(FieldName.GRID_P2_POWER, 1321),
                DecimalField(FieldName.GRID_P3_VOLTAGE, 1326, 1),
                IntField(FieldName.GRID_P3_POWER, 1327),

                # --- AC AUSGANG / LAST (Register 1500+) ---
                DecimalField(FieldName.AC_OUTPUT_FREQUENCY, 1500, 1),
                DecimalField(FieldName.AC_P1_VOLTAGE, 1511, 1),
                IntField(FieldName.AC_P1_POWER, 1512),               # Dein Wert 0x00D8 -> 216W
                DecimalField(FieldName.AC_P2_VOLTAGE, 1518, 1),
                IntField(FieldName.AC_P2_POWER, 1519),
                DecimalField(FieldName.AC_P3_VOLTAGE, 1525, 1),
                IntField(FieldName.AC_P3_POWER, 1526),
                UIntField(FieldName.AC_OUTPUT_TOTAL_POWER, 1532),    # Gesamtlast AC

                # --- TEMPERATUREN (In deinen Daten gefunden) ---
                DecimalField(FieldName.DEVICE_TEMPERATURE, 1101, 1), # Wechselrichter Temp
                DecimalField(FieldName.BATTERY_TEMPERATURE, 1102, 1),# Batterie Temp

                # --- EINSTELLUNGEN / CONTROL (Register 2000+) ---
                BoolField(FieldName.CTRL_AC, 2011),                  # AC Ausgang Schalter
                BoolField(FieldName.CTRL_DC, 2012),                  # DC Ausgang Schalter
                UIntField(FieldName.BATTERY_SOC_RANGE_START, 2022),  # Min SOC
                UIntField(FieldName.BATTERY_SOC_RANGE_END, 2023),    # Max SOC
                UIntField(FieldName.WORKING_MODE, 2013),             # Arbeitsmodus (Eco, UPS, etc.)
                
                # --- GRIDSCHUTZ & PARAMETER ---
                DecimalField(FieldName.GRID_VOLT_MIN_VAL, 2435, 1),
                DecimalField(FieldName.GRID_VOLT_MAX_VAL, 2436, 1),
                DecimalField(FieldName.GRID_FREQ_MIN_VALUE, 2437, 2),
                DecimalField(FieldName.GRID_FREQ_MAX_VALUE, 2438, 2),

                # --- GERÄTEINFORMATIONEN ---
                SwapStringField(FieldName.DEVICE_NAME, 12000, 8),
                SwapStringField(FieldName.SERIAL_NUMBER, 12008, 15),
                SwapStringField(FieldName.WIFI_NAME, 12002, 16),
            ],
        )
