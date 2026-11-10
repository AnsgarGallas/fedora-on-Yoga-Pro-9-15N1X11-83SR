# Kernel, Linux-Treiber und Veröffentlichungsrechte

[Übersicht](../README.md) · [Veröffentlichungsprüfung](publication-policy.md)

## Ergebnis der Vorprüfung

**Ein selbst gebauter Linux-Kernel und entsprechend lizenzierte Linux-Treibermodule sind grundsätzlich veröffentlichbar, wenn die jeweils geltenden Lizenzpflichten erfüllt werden.** Das ist keine pauschale Freigabe der vorhandenen Projektarchive. Für ein konkretes Release müssen tatsächlich enthaltene Dateien, Herkunft, Lizenzen und passender Quellcode einzeln geprüft werden. Die folgenden Regeln sind eine technische Compliance-Vorprüfung, keine individuelle Rechtsberatung.

Der Linux-Kernel steht als Gesamtwerk unter GPL Version 2; einzelne Dateien können kompatible oder alternative Lizenzen tragen. Die offizielle Kernel-Dokumentation verweist ausdrücklich auf diese Unterschiede.[1]

Die GPLv2 erlaubt die Weitergabe von Objektcode unter ihren Bedingungen und verlangt eine der in Abschnitt 3 beschriebenen Formen der Quellcodebereitstellung. Dazu gehören vollständige zugehörige Quellen einschließlich der zur Kompilierung und Installation verwendeten Skripte.[2]

## Konkrete Artefaktprüfung

Die [konkrete Releaseprüfung](release-audit.md) dokumentiert einen vollständig zusammengestellten und unabhängig geprüften lokalen experimentellen Grafik-/USB4-Kandidaten: Kernel, 150 Module, vollständige passende Quellen, Buildunterlagen und erforderliche Lizenz-/Änderungshinweise. Die geprüfte Metadatenbereinigung ist dort mit ihren Grenzen beschrieben. Die Artefakte sind noch nicht veröffentlicht; eine sichere native Installation ist weiterhin nicht freigegeben.

## Trennung der Bestandteile

| Bestandteil | Geplanter Umgang |
|---|---|
| Angepasster Linux-Kernel | Release erst mit vollständigem entsprechendem Quellpaket, Patches, Konfiguration, Build-/Installationsskripten und Lizenzhinweisen |
| Selbst gebaute Linux-Treibermodule | Je Datei Herkunft/Lizenz prüfen; passende Quellen, Änderungen und Buildunterlagen mitliefern |
| NVIDIA Open GPU Kernel Modules | Exakten Stand und einzelne Dateilizenzen prüfen; nicht mit dem gesamten NVIDIA-Treiberpaket gleichsetzen |
| NVIDIA-Bibliotheken und Firmware | Nicht Teil einer automatischen Freigabe für offene Kernelmodule; vorerst nur Bezugs-/Installationsweg nach gesonderter Prüfung dokumentieren |
| Extrahierte Windows-Treiber | Ausgeschlossen, keine Uploads oder Releaseanhänge |
| Aus Windows-Paketen entnommene Firmware und Lautsprechertuning | Ebenfalls nicht mitliefern; eine technische Formatprüfung ist keine Weiterverteilungserlaubnis |
| Anderweitig öffentlich erhältliche Firmware | Lizenz des konkreten Blobs separat prüfen; öffentliche Verfügbarkeit allein genügt nicht |
| Vorhandene Initramfs-/Bootarchive | Nicht übernehmen; können Schlüssel, individuelle Konfiguration und fremdlizenzierte Inhalte enthalten |
| Eigene Dokumentation | Öffentliche Dokumentationslizenz noch festzulegen; keine pauschale Umlizenzierung von Fremdcode |

Beim NVIDIA-Quellstand `615.78.08` nennt die `COPYING`-Datei grundsätzlich MIT für einzelne Dateien, soweit nicht anders vermerkt, und MIT/GPLv2 für das zusammengesetzte Linux-Kernelmodul. Das ist ein konkreter Ansatz für eine Modulveröffentlichung, keine Lizenzzusage für Firmware oder proprietäre Userspace-Bibliotheken.[3]

## Vorgesehener einfacher GPL-Releaseweg

Für dieses Projekt soll ein Binärrelease **zusammen mit dem vollständigen passenden Quellcode am selben Downloadort** angeboten werden. Die GPLv2 beschreibt gleichwertigen Zugang zum Quellcode am selben Ort ausdrücklich als mögliche Erfüllung bei Downloadverteilung.[2]

Ein Release soll mindestens enthalten:

- genaue Kernelbasis und festgehaltenen Quellstand;
- vollständigen zugehörigen Quellcode des veröffentlichten Builds, einschließlich aller enthaltenen Änderungen und externer Module;
- zusätzlich eine geordnete Patchserie zur leichteren Prüfung;
- tatsächlich verwendete Kernelkonfiguration und bereinigte Build-/Installationsskripte;
- Toolchain-/Buildumgebungsbeschreibung und Kernelrelease-/Modulzuordnung;
- alle erforderlichen Lizenztexte sowie erhaltene Copyright- und Änderungsvermerke;
- SHA256-Prüfsummen, Inhaltsmanifest und eine knappe Liste enthaltener beziehungsweise bewusst ausgeschlossener Komponenten;
- Releasebezogene Prüfergebnisse mit klarer Grenze zwischen Build, Boot, Bindung und echter Hardwarefunktion;
- additive Installations- und Rückfallanleitung ohne individuelle Gerätekennungen oder Schlüssel.

Nur auf einen beliebigen Upstream-Kernel zu verlinken oder allein die eigenen Patches bereitzustellen, wird hier **nicht als vollständiger Releaseweg vorausgesetzt**. Das zum Binärstand passende vollständige Quellpaket soll als eigenes Asset verfügbar sein. Ein allgemeiner GitHub-Quellarchivdownload des Dokumentationsrepos enthält diesen Kernelquellcode nicht automatisch.

## Technische und rechtliche Freigabeschranken

- Kein Kernel oder Modul wird allein wegen eines erfolgreichen Builds als sicher oder funktional beworben.
- Noch nicht hardwaregeprüfte Treiber werden eindeutig als experimentell gekennzeichnet; reine Refusal-/Auditmodule sind keine nutzbare Audiolösung.
- Fehlende Audio-/Kamerafunktion wird in Releasehinweisen nicht verschwiegen.
- Modulkompatibilität wird gegen den vorgesehenen Kernel geprüft; eine gleiche Versionsnummer allein reicht nicht.
- Eingebettete Firmware, Zertifikate, Debugpfade und weitere Binärmetadaten werden vor einem Upload geprüft. Private Schlüssel bleiben immer ausgeschlossen.
- Wo Rechte an Quellbestandteilen, Firmware, Tuningdaten oder aus Binäranalyse abgeleiteten Bestandteilen ungeklärt sind, bleibt die betroffene Datei bis zur Klärung ausgeschlossen. Selbst kompilierter Code wird dadurch nicht automatisch zum eigenen frei lizenzierbaren Werk.

**Aktueller Stand:** Ein vollständiger Releasekandidat ist lokal vorbereitet und unabhängig geprüft; Binärdateien und Kernelquellen sind noch nicht öffentlich verfügbar. Controller und Prozessrunner sind separat unter GPL-2.0-only vorbereitet, aber weder Bestandteil des Sieben-Archiv-Satzes noch eine native Startfreigabe.

## Sources

[1] https://www.kernel.org/doc/html/latest/process/license-rules.html
[2] https://raw.githubusercontent.com/torvalds/linux/master/LICENSES/preferred/GPL-2.0
[3] https://raw.githubusercontent.com/NVIDIA/open-gpu-kernel-modules/615.78.08/COPYING
