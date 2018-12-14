ALTER TABLE Elves
ADD shortlist TEXT;

SELECT CONCAT(INITCAP(firstname), ' ', INITCAP(lastname)) AS shortlist
FROM Elves
WHERE firstname LIKE '%tegil%'
  OR lastname LIKE '%astar%';
