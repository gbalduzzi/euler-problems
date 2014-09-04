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
 * @author Santo Antonio Terranova (@tng46)
 * @version 1.1.0
 * 
 * For isPalindrome() function i prefer String approach.
 * I have increased algorithm performance by simply changing the conditions order.
 * Try to flip order to see the difference.
 */
   

    $startTest = microtime();
  
    $maxPalindrome = 0;
    for ($i=999; $i>100; $i--)
        for ($j=999; $j>100; $j--)
            if ( $i*$j > $maxPalindrome && isPalindrome($i*$j) )       //Try to flip order to see the performance difference
                $maxPalindrome = $i*$j;

    function isPalindrome($num) {
        if ( strcmp($num, strrev($num)) == 0 )  
            return true;                        //..is palindrome!

        return false;
    }

    $endTest = microtime();
    echo "Test time: ". ($endTest - $startTest) . "\n";
