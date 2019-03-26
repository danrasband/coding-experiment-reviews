/**
 * Given an array of N integers, find the count of the highest integer.
 *
 * @param {*} A
 */
function solution(A) {
  // Quick base cases.
  if (!Array.isArray(A)) {
    return 0;
  } else if (A.length === 0) {
    return 0;
  }

  // Sort the array in reverse order. The first element will then be the highest
  // integer. We'll double check that the given values are all integers.
  const sorted = A.sort((a, b) => {
    const numA = Number(a);
    const numB = Number(b);

    if (!Number.isInteger(numA) || !Number.isInteger(numB)) {
      throw new Error("Unexpected input, only integers are supported");
    }

    return b - a;
  });

  // We can now find the frequency of the highest integer as we traverse the
  // array. Finally, we can exit early if the value seen as we traverse changes
  // from the highest.
  const highest = sorted[0];
  var count = 0;

  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] === highest) {
      count += 1;
    } else {
      break;
    }
  }

  return count;
}
