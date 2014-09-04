<?php
/**
 * Problem 24 from Project Euler
 * 
 * A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
 * If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
 * The lexicographic permutations of 0, 1 and 2 are:
 * 
 * 012   021   102   120   201   210
 * 
 * What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 * 
 * REGARDING THE PERFOMANCE
 * This is not the final version of the Algorithm, anyone can improve it.
 * If you have a better solution please submit a pull request, or an issue, on Github.
 * 
 * @author Claudio Ludovico Panetta (@Ludo237)
 * 
 * @version 1.0.0
 **/
define("NUMBERS", 10);
define("LIMIT", 1000000);
// Helper variables
$maxNumber = LIMIT;
$digits = range(0, (NUMBERS - 1)); // as we have 0...
$permutation = [1 => 1];
$results = [];
// Algorithm starts
print("Algorithm starts, please wait\n");
// Iterating trough the list of our number
// And creating the permutation...
for($i = 2; $i < NUMBERS; $i++){
    $permutation[$i] = $permutation[$i - 1] * $i;
}
// ... with a little help from PHP :-)
$permutation = array_reverse($permutation);

foreach($permutation as $number){
    $results[] = floor($maxNumber / $number);
    $maxNumber %= $number;
}
// Print the digits for the Lexicographic order
/*foreach($results as $result){
    print($digits[$result]);
    // Unset the digit so we can re-arrange our array
    unset($digits[$result]);
    sort($digits);
}
print("$digits[0]\n");*/
// Algorithm end
print("Algorithm end.\n");

?>
