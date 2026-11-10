# NVIDIA-Grafik und KDE

[Leitfaden](../guide.md) · [Status](../status.md)

## Schichten getrennt prüfen

Ein sichtbarer Firmware-Framebuffer ist kein Nachweis eines gebundenen NVIDIA-Treibers. Ebenso belegt eine erfolgreiche Modulinitialisierung weder Rendering noch einen stabilen Desktop. Im Projekt wurden Speicher-Metadaten, Kernelbindung, DRM/KMS, EGL/OpenGL ES und der reguläre KDE-Start getrennt geprüft.

Der bestätigte Pfad verwendet **NVIDIA 615.78.08** mit dazu passenden ARM64-Bibliotheken und Firmware. Quellen der offenen Kernelmodule sind nicht mit proprietären Bibliotheken oder Firmware gleichzusetzen; die Veröffentlichung wird getrennt geprüft. Siehe [Lizenzprüfung](../distribution.md).

## Speicher-Metadaten als konkrete Voraussetzung

Die tatsächliche Yoga-Firmware lieferte GPU-reservierte Speicherbereiche. Ein vollständiger Test ihrer Seiten-Metadaten fand eine Lücke; ein gezielt begrenzter, bis zum Neustart residenter PRIVATE-Memmap-Workaround ergänzte die fehlenden Beschreibungen. Erst danach wurde erneut der komplette relevante Bereich geprüft.

Das ist **kein genereller Speicherkorrekturtrick**. Reservierte Ressourcen, IOMMU-Zuordnung, fehlende gegenüber bereits vorhandenen Metadaten und Lebensdauer müssen auf genau dem getesteten Firmwarestand übereinstimmen. Hier werden bewusst keine ungeschützten Schreib-/Ladebefehle oder übertragbare Speicheradressen angeboten. Der Workaround ist noch nicht als öffentlich nutzbares Paket freigegeben.

## Vom Renderingtest zum normalen Desktop

Ein isolierter EGL-Test belegte NVIDIA-basiertes Offscreen-Rendering; erst die nachfolgende reguläre KDE-Sitzung belegte die Desktopintegration. Capability-behaftete Desktopprozesse folgen nicht denselben Bibliothekssuchregeln wie ein gewöhnlicher Testprozess. Ein erfolgreicher Test mit abweichendem Bibliothekspfad genügt deshalb nicht für die Systemintegration.

Eine weitere konkrete Fehlerursache war das SELinux-Dateilabel privater Kernelmodule: Der systemd-Start durfte Module mit Bibliothekslabel nicht laden. Ein korrektes Modul-Label und dessen Vorabprüfung lösten diesen Startfehler im geprüften Pfad, ohne SELinux zu deaktivieren.

## Bestätigt und nicht bestätigt

- Bestätigt: Originaltreiber 615.78.08, regulärer KDE-/OpenGL-ES-Betrieb, normale Helligkeit nach Neustart.
- Nicht gelöst: Suspend/Resume und belastbare Langzeitstabilität.
- Historisch beobachtet: Flip-Timeouts und Warnungen bei isolierten Abschaltversuchen. Ein erfolgreicher normaler Desktopstart macht diese Befunde nicht rückwirkend gegenstandslos.
- Experimentelle Reparaturvarianten aus der Abschaltdiagnose gehören nicht zum akzeptierten Originaltreiberpfad.

## Nachweisgrenze und nächste Veröffentlichung

Die Aussagen stammen aus den internen Grafik- und Bootprüfungen; deren Rohdaten sind nicht öffentlich enthalten. Vor einer nachbaubaren Veröffentlichung müssen die bereinigten Helfer, tatsächlichen Quellen, Abhängigkeiten und Sicherheitsgrenzen separat geprüft werden. Es gibt hier noch kein NVIDIA-Gesamtpaket zum Herunterladen.
