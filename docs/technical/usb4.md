# USB4-Plattformintegration

[Leitfaden](../guide.md) · [Status](../status.md)

## Controller anhand tatsächlicher ACPI-Geräte finden

`CONFIG_USB4=y` allein stellt keine Plattformunterstützung sicher. Im Yoga sind passende NHI-Plattformgeräte unter **NVDA8100** vorhanden. Das ebenfalls sichtbare **NVDA300A** ist für sich weder ein Nachweis des benötigten NHI-Treibers noch ein Grund, einem Registerzugriffe ausführenden Treiber ungeprüft eine neue Hardware-ID hinzuzufügen.

Der untersuchte Kernelpfad benötigt zusätzlich die passenden Plattform-NHI-, SSPM- und Power-Wrap-Abhängigkeiten. Die Einstellung `power_wrap_drv.usb4_release=0` gehörte zum getesteten Ressourcen-Erhaltungsvertrag; sie ist ohne den zugehörigen konkreten Treiberstand keine allgemeine Reparaturanweisung.

## FF-A, ACPI und UCSI als eigene Fehlerkette

Ein Fehler in der Interruptabbildung verhinderte einen Teil der Firmwarebenachrichtigungen. Die Korrektur behandelte einen von der Firmware gelieferten SGI als solchen über den bestehenden GIC-Root-Fwnode, statt ihn pauschal als ACPI-GSI abzubilden. Die gelieferte Interruptnummer blieb unverändert; ein geratener numerischer Offset wäre keine Lösung.

Nach dem separaten Kernelbau und tatsächlichem Boot band das betreffende FF-A-Gerät, und UCSI registrierte Ports ohne den vorherigen Initialisierungstimeout. Einzelne weitere Interruptwarnungen waren damit nicht automatisch behoben.

## Abnahmestufen

1. Plattform-NHI bindet und Hostrouter sind vorhanden.
2. Firmware-/UCSI-Benachrichtigungen initialisieren.
3. Ein realer USB4-Link wird aufgebaut und ist beobachtbar.
4. Gewünschte Betriebsarten werden einzeln funktional geprüft.

Der Projektstand reicht bis zum nachgewiesenen Link und geprüften Transport. Das ist keine pauschale Freigabe aller USB4-Funktionen. Konkrete angeschlossene Geräte, Netzwerkkonfiguration und Gegenstellen sind nicht Gegenstand dieser Dokumentation.

## Noch bereitzustellen

Öffentlich fehlen die exakt zugeordneten Plattformpatches, die bereinigte FF-A-Korrektur, Konfiguration und Build-/Bootreproducer. Die vorliegende Beschreibung dokumentiert Ursache und Lösungsrichtung, ist aber noch kein vollständiges öffentlich nachbaubares Kernelpaket.
