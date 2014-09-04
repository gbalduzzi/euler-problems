<?php
/***********************************
 *
 * Problem 1 from Project Euler
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiplies is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000
 *
 * This file is made with VIM using PHP 5.6.0a3 on HHVM machine
 *
 * PLEASE NOTE
 * In order to work you must have, at least, PHP 5.3.x or higher
 *
 * REGARDING THE PERFORMANCE
 * This is not the final version, as you can see I'll trace the version of every solution, so please don't think that
 * this is the best algorithm in terms of speed and code optimization, for any trouble open an issue.
 *
 * @author Pietro Arturo Panetta (arturu.it)
 * @author Claudio Ludovico Panetta (@Ludo237)
 * @version 1.5.1
 *************************************/

// This solution involing Gauss

// Start the benchmark
$startTest = microtime();

// We need a scalable algorithm so we cannot use a static zise for our test
$end = 1000;
$start = 0;

// Lower the end by a factor of one in order to server all the multiples of x
// minus the $end
--$end;

/** --- Functions ---- **/
// Please Note high() and lower() are strictly similar, but if we keep them separate they
// are more readable

/**
 * function higher
 * @param $end
 * @param $reason
 * @description
 *  Find the higher multiple
 **/
function higher ($reason, $end) {
    // Starting from the higher i lower by a factor of one
    // untile we found the higher multiple
	for ( $i = $end; ; $i--){
		if ( $i % $reason == 0 )
			return $i;
	}
}

/**
 * function lower
 * @param $start
 * @param $reason
 * @description
 *  Find the lower multilple
 **/
function lower ($reason, $start){
	// if start is zero we need to fix it
	$start = ($start == 0) ? ++$start : $start;

    // Starting from the beginning
    // we add by a factor of one until we found the lower multiple
	for ($i = $start; ; $i++){
		if ( $i % $reason == 0 )
			return $i;
	}
}

/**
 * function iterations
 * @param $lower
 * @param $higher
 * @param $reason
 * @description
 *  Iterations is how many times we found the multilple inside our serie
 **/
function iterations ($reason, $higher, $lower){
    // return the number of iterations
    // when $start == 0 -> (n - 1)
    return $higher / $reason;
}


/**
 * function trapeziusArea
 * @param $end
 * @param $start
 * @param $reason
 * @description
 *  Thanks to Gauss and his idea where the sum of numbers inside
 *  a progression is equal to trapezius area we can identify our
 *  result base on it.
 **/
function trapeziusArea($reason, $start, $end) {
	$majorBase = higher($reason, $end);
	$minorBase = lower($reason,$start);
	// 3*1 + 3*2 + 3*3 + ... 3(n-3) + 3(n-2) + 3(n-1) + 3(n-0)
    // equal to: h * (majorBase + minorBase) / 2
    // Awesome!
	return iterations($reason, $majorBase, $minorBase) * ($majorBase + $minorBase) / 2;
}

/** ---- Calculating areas of different sequences ----- **/
$sumOfThree = trapeziusArea(3, $start, $end);

$sumOfFive = trapeziusArea(5, $start, $end);

$overlappingMultiples = trapeziusArea( 3*5 ,$start, $end);


$total = $sumOfThree + $sumOfFive - $overlappingMultiples;

// End of benchmark
$endTest = microtime();
echo "Algorithm time: ". ($endTest - $startTest);
