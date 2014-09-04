/***********************************
 *
 * Problem 3 from Project Euler
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 *
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
 * @version 1.1
 *************************************/

// Start the benchmark
var startTime = Date.now();


// var target = 13195;
var target = 600851475143;

var primeFactors = [];

while(target > 1) {
    for(var i = 2; i <= target; i++)
        if(target % i === 0) {
            target /= i;
            primeFactors.push(i);
            break;
        }
}


var maxPrimeFactor = Math.max.apply(null, primeFactors);

// End of benchmark
var endTime = Date.now();
console.log('Algorithm time: ' + (endTime - startTime));
