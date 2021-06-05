/*SQL with LOTR: Elven Wildcards

You have been asked to create a shortlist of candidates for a recently
vacated position on the council.

Choose those with tegil appearing anywhere in their first name,
as they are likely to be good calligraphers, OR those with astar anywhere
in their last name, who will be faithful to the role.

Return the firstname and lastname column concatenated, separated by a space,
into a single shortlist column, and capitalise the first letter of each name.*/

ALTER TABLE Elves
ADD shortlist TEXT;

SELECT CONCAT(INITCAP(firstname), ' ', INITCAP(lastname)) AS shortlist
FROM Elves
WHERE firstname LIKE '%tegil%'
  OR lastname LIKE '%astar%';
