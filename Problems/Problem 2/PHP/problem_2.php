<?php
/***********************
 *
 * Problem 2 from Project Euler
 *
 * Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms
 * will be:
 *  
 *  1,2,3,5,8,12,21,34,55,89, ...
 *
 * By considering the terms in the Fibonacci sequence whose values do no exceed four million, find the sum of the even-valued terms
 *
 * PLEASE NOTE
 * In order to work you must have, at least, PHP 5.3.x or Higher
 *
 * REGARDING THE PERFORMANCE
 * This is not the final version of the scritp, you can improve the algorithm by submitting a pull request or an issue on Github.
 * Feel free to ask for anything on Github.
 *
 * @author Claudio Ludovico Panetta (@Ludo237)
 * @version 1.0.0
 **************************/

// Start the benchmark
$startTest = microtime();

// As always we cannot "fixed" the size of our algorithm
$size = 32; // Fibonacci numbers, you can change it

// We need to privots as starting point, the array idea seems bit faster
$pivot = array(1,2);

// And, of course, a list of the fibonacci numbers
$fibonacci = array();
$total = 0;

// Main algorithm part starts here
for($i = 0; $i < $size; $i++) {
    if( $i != 0 && i != $size)
        $fibonacci[$i] = $fibonacci[$i-1]+$fibonacci[$i-2];
    elseif($i == 1)
        $fibonacci[$i] = $pivot[1];
    else
        $fibonacci[$i] = $pivot[0];
    // Sum the numbers now
    if($fibonacci[i] % 2 == 0)
        $total += $fibonacci[i];
}

// Algorithm end
$endTest = microtime();
echo "Test time: ". ($endTest - $startTest). "\n";
