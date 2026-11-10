# Veröffentlichungs- und Datenschutzgrenzen

[Übersicht](../README.md) · [Releaseanforderungen](distribution.md)

## Inhaltlicher Umfang

Veröffentlicht werden nur hardwarebezogene Voraussetzungen, Untersuchungsschritte, technische Erkenntnisse, Linux-Lösungen und deren tatsächlicher Abnahmestand für das Yoga Pro 9 15N1X11 (83SR). Keine persönliche Einrichtung und keine Informationen über weitere Geräte.

Zulässig sind etwa Modellfamilie, nicht individuelle ACPI-/PCI-/Codec-IDs, Treiberversionen, Kerneloptionen sowie bereinigte Tests mit künstlichen neutralen Beispieldaten. Hardwaremodell-IDs sind von Seriennummern und anderen eindeutigen Gerätekennungen zu unterscheiden.

## Nicht übernehmen

- Namen, Benutzernamen, E-Mail-Adressen, lokale Home-/Projektpfade oder Hostnamen aus der privaten Arbeitsumgebung;
- Seriennummern, individuelle Geräte-/Silizium-IDs, machine-id, Boot-IDs, Datenträger-UUIDs oder rohe Firmwarevariablen;
- IP-/MAC-Adressen, Netzwerk-/VPN-Konfiguration, SSH-Schlüssel, Tokens, Passwörter, Wiederherstellungsschlüssel oder TPM-Entsperrdaten;
- persönliche Profile, Sitzungen, Gesprächsprotokolle oder unbereinigte Bildschirmfotos;
- komplette Journale, DMI-/ACPI-/EFI-Dumps, private Boot-/Installerarchive und vorhandene Initramfs-Dateien;
- extrahierte Windows-Treiber, DriverStore-Archive und daraus entnommene Firmware-/Tuningdateien ohne gesonderte Rechteprüfung.

**Keine Massenkopie des Entwicklungsprojekts.** Öffentliche Dateien werden gezielt ausgewählt oder neu aus belegten technischen Erkenntnissen formuliert. `.gitignore` ersetzt weder Inhaltsprüfung noch Bereinigung der Git-Historie.

## Prüfung vor Commit und Veröffentlichung

1. Nur die beabsichtigten Dateien auswählen; keine pauschale Übernahme privater Verzeichnisse.
2. Inhalte und Dateinamen auf Geheimnisse, Identitätsmerkmale, weitere Hardware und unnötige personenbezogene Angaben prüfen.
3. Lokale Links, Statusaussagen und Nachweisgrenzen kontrollieren. Offline-Test, Build und Hardwarefunktion getrennt ausweisen.
4. Bei Code Urheber-/Lizenzvermerke nicht zur Anonymisierung entfernen: Bestehende rechtlich erforderliche Fremdvermerke bleiben erhalten; konfliktbehaftete Dateien bleiben bis zur Klärung draußen.
5. Binärmetadaten prüfen: Buildbenutzer/-host, absolute Debugpfade, eingebettete Zertifikate und Buildinformationen können Angaben enthalten, die in Markdown nicht sichtbar sind. Keine vorhandenen privaten Builds blind hochladen.
6. Initramfs nur für eine Veröffentlichung eigens erzeugen und auf enthaltene Schlüssel, Konfiguration und Firmware prüfen; bevorzugt lokale Erzeugung beim Anwender dokumentieren.
7. Auch Commit-Autor/-E-Mail und bestehende Git-Historie sind öffentlich sichtbar. Keine Identität erfinden oder Git-Konfiguration still ändern; vor einem Commit die gewünschte öffentliche Autorenidentität festlegen.
8. Remote-Push und Release getrennt von lokaler Vorbereitung prüfen. Ein lokaler Entwurf ist noch keine Veröffentlichung.

## Geltung

Diese Regeln gelten ebenso für Issues, Pull Requests, Anhänge und Releaseassets. Neue technische Befunde werden erst nach Prüfung übernommen; laufende oder abgebrochene Tests werden nicht als Erfolg ausgegeben.
