---
title: "DeyeCloud"
weight: 20
translationKey: "deye-cloud"
---

# DeyeCloud

{{< badge "deye-only" >}}

DeyeCloud to zapasowa metoda połączenia dostępna dla instalacji typu **Solarman**. Może być używana jako backup w przypadku problemów z Solarman lub jako jedyne połączenie.

## Tryby działania

| Tryb | Opis |
|------|------|
| **Wyłączone** | DeyeCloud nie jest używane |
| **Włączone** | DeyeCloud aktywuje się automatycznie, gdy Solarman zgłosi błąd |
| **Tylko zapasowe** | Nie używaj Solarman — zawsze DeyeCloud |

## Konfiguracja

1. W sekcji **Zapasowe połączenie — DeyeCloud** parametrów instalacji wybierz tryb działania
2. Wprowadź **dane logowania** do DeyeCloud (mogą być inne niż do Solarman)
3. Zaznacz **Zapamiętaj dane do logowania** — bez tego wymagane ręczne ponowne logowanie
4. Po połączeniu wybierz **SerialNo falownika**

Szczegółowy opis parametrów znajdziesz w [Parametry instalacji]({{< relref "/instalacja/parametry-instalacji" >}}).

> [!NOTE]
> DeyeCloud i Solarman to dwa niezależne portale z osobnymi danymi logowania. Upewnij się, że masz konto w obu serwisach, jeśli chcesz korzystać z zapasowego połączenia.
