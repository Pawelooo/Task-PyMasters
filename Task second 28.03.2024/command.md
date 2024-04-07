# Command 

Wymagania

1. Klasy Podstawowe:
Employee: Klasa reprezentująca pracownika. Powinna zawierać podstawowe informacje takie jak imię,
nazwisko, identyfikator pracownika oraz dział.
Department: Klasa reprezentująca dział w firmie. Powinna zawierać nazwę działu i listę pracowników
przypisanych do tego działu.

2. Klasy Raportów:
ReportGenerator: Klasa abstrakcyjna lub interfejs dla generatorów raportów. Powinna określać metodę
generate_report(), którą każdy konkretny generator raportów będzie implementować.
Implementacje ReportGenerator dla różnych typów raportów, na przykład:
EmployeeReportGenerator: Generuje raport dla pojedynczego pracownika.
DepartmentReportGenerator: Generuje raport dla całego działu, zawierający informacje o
wszystkich pracownikach w dziale.

3. Kompozycja:
Użyj kompozycji, aby umożliwić elastyczne generowanie raportów. Na przykład, obiekty klasy Employee i
Department mogą zawierać referencję do odpowiedniego ReportGenerator, który będzie używany do
generowania raportów.


### PyMasters
https://github.com/pymasterspl/
https://pymasters.pl/