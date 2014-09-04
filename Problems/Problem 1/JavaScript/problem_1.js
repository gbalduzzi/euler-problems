/***********************************
 *
 * Problem 1 from Project Euler
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiplies is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000
 *
 * This file is made with Sublime Text 2
 * 
 * PLEASE NOTE
 * In order to work you must have one of following browsers: Chrome, Firefox, IE9+, Opera 10.5+, Safari 4.0+, all mobile browsers
 * and nodejs of course.
 *
 * REGARDING THE PERFORMANCE
 * This is not the final version, as you can see I'll trace the version of every solution, so please don't think that
 * this is the best algorithm in terms of speed and code optimization, for any trouble open an issue.
 *
 * @author Matteo Manchi (@matteomanchi)
 * @version 1.0.0
 *************************************/

// Start the benchmark
var startTime = Date.now();

// We need a scalable algorithm so we cannot use a static size for our test
var size = 1000;

// First of all we create an Array of `size` length with all values as `undefined`.
// We will iterate using indexes
var total = Array.apply(null, Array(1000))

// Then we use the `reduce` method with anonymous callback function(total, currentValue, index);
// in this way we will iterate the array only one time.
    .reduce(function (total, currentValue, index) {
        return index % 3 === 0 || index % 5 === 0 ? total + index : total;
    }, 0);

// End of benchmark
var endTime = Date.now();
console.log('Algorithm time: ' + (endTime - startTime));