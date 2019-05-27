/**
 * Returns a new integer that is the reverse of the digits of the first.
 *
 * @param {*} X A 32-bit integer to be reversed.
 */
function solution(X) {
  if (!Number.isInteger(X)) {
    throw new Error("Invalid input");
  }

  const original = `${X}`;
  const isNegative = original.startsWith('-');

  const sanitized = original.replace(/\s/, '').replace(/[\-\,]/, '');
  const reversed = sanitized.split('').reverse().join('');

  return isNegative
    ? -1 * Number(reversed)
    : Number(reversed);
}
