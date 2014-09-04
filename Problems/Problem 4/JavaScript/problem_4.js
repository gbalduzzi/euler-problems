/***********************************
 *
 * Problem 4 from Project Euler
 * 
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.

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
 * @version 1.0
 *************************************/


 function isPalindromic(n) {
    return n.toString() === n.toString().split('').reverse().join('');
}

var startTime = Date.now();

var numberOfDigits = 3;
var upperBound = Math.pow(10, numberOfDigits) -1;

var result = false;

var i = upperBound,
    j = upperBound,
    max = 0;


// the condition `i >= j` take down this execution time from ~200ms to ~30ms
for(i = upperBound; i > 0 && i >= j; i--) {
    result = false;
    for(j = upperBound; j > 0 && result === false; j--) {
        var mult = i * j;
        result = isPalindromic(mult);

        if(result && max < mult)
            max = mult;
    }
}

// End of benchmark
var endTime = Date.now();
console.log('Algorithm time: %dms', (endTime - startTime));