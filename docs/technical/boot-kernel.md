# Boot und angepasster Kernel

[Leitfaden](../guide.md) · [Status](../status.md)

## Modellabgrenzung und erste Bestandsaufnahme

Die Dokumentation gilt für das Yoga Pro 9 15N1X11, Modellfamilie 83SR. Vergleichbare Marketingnamen reichen zur Übertragung von Patches nicht aus. Die folgenden Abfragen lesen nur ausgewählte, nicht eindeutige Hardware-/Kernelmerkmale:

```sh
uname -m
uname -r
cat /sys/class/dmi/id/product_name
cat /sys/class/dmi/id/product_version
```

Vor einem veröffentlichten Fehlerbericht trotzdem jede Ausgabe prüfen. Vollständige DMI-, ACPI-, Journal- oder Bootparameter-Dumps gehören nicht ungeprüft in ein Issue.

## Sichtbare Konsole statt vermeintlich eingefrorener Entsperrung

Im untersuchten Bootpfad waren virtuelle Terminals vorhanden, aber die Systemkonsole nicht korrekt nutzbar. Ein Plymouth-Bypass allein genügte nicht. Der funktionierende angepasste Eintrag enthielt:

```text
console=tty0 plymouth.enable=0 "acpi_osi=!Windows 2022"
```

Das ist ein **Ausschnitt**, keine vollständige Kernelkommandozeile. Vorhandene Root-, Verschlüsselungs- und sonstige Optionen dürfen nicht ersetzt werden. Die ACPI-OSI-Einstellung gehört zum getesteten Pfad; ein isolierter Kausalnachweis für jede einzelne Option liegt damit nicht vor. Erfolgreich war der tatsächliche Start mit sichtbarer Entsperrung und anschließendem Desktop, nicht bloß die Erstellung des Eintrags.

Fedora-Bootgeneratoren können Optionen aus `/etc/default/grub` bzw. `/etc/kernel/cmdline` neu erzeugen. Nach einer späteren Änderung müssen der konkrete BLS-Eintrag und die tatsächlich verwendeten Parameter erneut zusammenpassen. Individuelle Root-/LUKS-Kennungen werden hier nicht bereitgestellt.

## Bau und ABI sind Teil der Lösung

- Ausgangsquellen, Patchreihenfolge, Kernelkonfiguration und Toolchain müssen genau bezeichnet werden.
- Für externe Module gehören Kernelrelease, Architektur, `vermagic`, Exporte/Importe und vollständige Modulabhängigkeiten zur Prüfung.
- Im untersuchten Audio-Testkernel ist `CONFIG_MODVERSIONS` deaktiviert. Es gibt daher keine behauptete symbolweise CRC-Absicherung; ein passendes Release allein ersetzt die übrige ABI-Prüfung nicht.
- Build, Paket, Installation und tatsächlicher Boot sind eigenständige Abnahmen.

## Rückfall und Grenzen

Neue Versuche wurden additiv mit getrennten Booteinträgen und geschützten vorhandenen Artefakten durchgeführt. Der akzeptierte Booteintrag `7.2.8-yoga-nvidia` verwendet tatsächlich den kompilierten Kernel `7.2.8-yoga-usb4-v2`; Booteintragsname und Kernelrelease sind nicht gleichzusetzen. Die [konkrete Releaseprüfung](../release-audit.md) dokumentiert die Imagezuordnung. Ein einmaliger Teststart ist von einer Änderung des dauerhaften Standards zu unterscheiden. Es wird hier noch kein allgemeines Installationsskript veröffentlicht, weil die bisherigen internen Helfer geräteindividuelle Schutzprüfungen und nicht öffentliche Konfiguration enthalten.

**Noch bereitzustellen:** bereinigter Quell-/Patchstand, Buildkonfiguration und Reproducer für das spätere öffentliche Release. Dieser Text allein rekonstruiert noch keinen bitidentischen Kernel.
