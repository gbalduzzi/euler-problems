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
 * @author Claudio Ludovico Panetta (@Ludo237)
 * @version 1.5.0
 *************************************/

// ALGORITHM NOT TESTED YET, IF YOU TEST IT PLEASE REPORT EVERYTHING ON GITHUB.

// Start the benchmark
$startTest = microtime();

// We need a scalable algorithm so we cannot use a static zise for our test
$size = 1000;

$i = 0;
$sum = 0;

do
{
	$sum += $i;
	$i += 3;
} while ($i < $size);
$i = 0;
do
{
	$sum += $i;
	$i += 5;	
} while ($i < $size);
$i = 0;
do
{
	$sum -= $i;
	$i += 15;	
} while ($i < $size);

$endTest = microtime();
echo "Algorithm time: ". ($endTest - $startTest);
