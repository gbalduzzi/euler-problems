<?php
/**
 *
 * Problem 4 from Project Euler
 *
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 *
 *
 * PLEASE NOTE
 * In order to test this script you must have PHP 5.3+ installed and php-cli, to test it with a terminal.
 *
 * REGARDING THE PERFORMANCE
 * This is not the final version, as you can see I'll trace the version of every solution, so please don't think that
 * this is the best algorithm in terms of speed and code optimization, for any trouble open an issue.
 *
 * @author Pietro Arturo PAnetta (@arturu)
 * @author Santo Antonio Terranova (@tng46)
 * @version 1.0
 */

// Starting the benchmark
$startTime = microtime();

// thanks to Santo Antonio Terranova @tng46
function isPalindrome($num){

	if ( strcmp($num, strrev($num)) == 0 )  
            return true;                        //..is palindrome!

        return false;
}

function cycleManager($coppia,$command){

	if ( $command == 'break' ){
		--$coppia['a'];
		$coppia['b']=999;
	}
	else
		--$coppia['b'];

	if ( $coppia['a'] < 100 )
		$coppia['cycle']=false;

	return $coppia;
}


function maxPalindrome($coppia){

	$maxPalindrome = 0;

	$coppia['cycle']=true;

	do {

		$number = $coppia['a'] * $coppia['b'];

		if ( isPalindrome( $number ) ) {
			$maxPalindrome = ( $number > $maxPalindrome ) ? $number : $maxPalindrome;
			$coppia = cycleManager($coppia,'break');
		}

		else 
			$coppia = cycleManager($coppia,'continue');

	} while ($coppia['cycle']);
	

	return $maxPalindrome;
}


$result = maxPalindrome( array('a'=>999,'b'=>999) );

// Finish the benchmark 
$endTime = microtime();
echo "Algorithm time: ". ($endTime - $startTime);
