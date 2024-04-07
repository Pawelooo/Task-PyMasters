# Command 

Zadanie domowe: Zastosowanie zasad SOLID w Pythonie
Cel zadania:

Celem tego zadania jest praktyczne zastosowanie zasad SOLID w języku programowania Python. Uczestnicy powinni
zaimplementować przykładowy system, demonstrując zrozumienie i umiejętność stosowania zasad SOLID do
poprawy czytelności, skalowalności i utrzymania kodu.

Opis zadania:

Wyobraź sobie, że tworzysz system do zarządzania biblioteką książek. System powinien umożliwić dodawanie książek
do katalogu, wyszukiwanie książek po różnych kryteriach oraz wypożyczanie i zwracanie książek przez użytkowników.
Twoim zadaniem jest zaprojektowanie i zaimplementowanie podstawowych komponentów tego systemu,
przestrzegając zasad SOLID.

Wymagania

1. Zasada pojedynczej odpowiedzialności (SRP):
Utwórz klasę Book, która będzie przechowywać informacje o książkach (np. tytuł, autor, ISBN).
Zaimplementuj klasę LibraryCatalog, która będzie zarządzać dodawaniem i wyszukiwaniem książek w
katalogu.
 
2. Zasada otwarte/zamknięte (OCP):
Rozszerz funkcjonalność wyszukiwania książek, umożliwiając wyszukiwanie nie tylko po tytule i autorze, ale
także po roku wydania, bez modyfikacji istniejącego kodu LibraryCatalog.

3. Zasada podstawienia Liskov (LSP):
Utwórz klasę User oraz klasę pochodną Member, która dodaje funkcjonalność wypożyczania książek.
Użytkownik typu Member powinien być w stanie zastąpić użytkownika typu User bez wpływu na działanie
systemu.

4. Zasada segregacji interfejsu (ISP):
Zdefiniuj interfejsy dla różnych typów zachowań systemu, np. Searchable, Borrowable, tak aby klasa
Book implementowała tylko te funkcje, które są dla niej sensowne.

5. Zasada odwrócenia zależności (DIP):
Wprowadź abstrakcje, które odwrócą zależność między wysokopoziomowymi operacjami a szczegółami
implementacji wyszukiwania i wypożyczania książek. Na przykład, LibraryCatalog powinien zależeć od
abstrakcyjnego interfejsu SearchStrategy, a nie od konkretnych implementacji algorytmów wyszukiwania.
25/29

Dodatkowe informacje:

Przy implementacji klasy LibraryCatalog zastanów się, jak przechowywać książki, aby ułatwić ich
wyszukiwanie według różnych kryteriów.

Pamiętaj o testach jednostkowych sprawdzających poprawność działania kluczowych komponentów systemu.

Zwróć uwagę na to, jak można by dodać nowe funkcjonalności do systemu w przyszłości (np. zarządzanie stanem
wypożyczonych książek), przestrzegając zasad SOLID.

### PyMasters
https://github.com/pymasterspl/