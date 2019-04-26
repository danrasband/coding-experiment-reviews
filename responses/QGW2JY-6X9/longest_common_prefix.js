/**
 * Returns the maximum product of X consecutive integers in B.
 *
 * @param {*} X count of conesecutive integers.
 * @param {*} B zero-indexed array of integers.
 */
function solution(X, B) {
  // Sanitize the count.
  const count = Number(X);

  // Weird cases...
  if (!Number.isInteger(X) || !Array.isArray(B)) {
    throw new Error("Invalid input");
  } else if (B.length <= 0) {
    return undefined;
  }

  // Edge case, return the largest integer in the array.
  if (count === 1) {
    return B.sort((a, b) => b - a)[0];
  }

  return B.reduce((largest, currentVal, index, remaining) => {
    const end = index + count;
    const prod = B.slice(index, end).reduce((prod, val) => prod * val, 1);

    return prod > largest
      ? prod
      : largest;
  }, 0);
}
