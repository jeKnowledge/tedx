/**
 * @function flooper
 *
 * @param {String|HTMLElement} flooperElement - flooper container, defaults to '.js-flooper'
 * @param {Object} [options] - containing the props described here at #options-and-defaults
 */

/**
* @param {Object} options
*
* @param {bool}   [options.autoPlay=true] - flooper starts playing at initialisation
* @param {string} [options.flooperItemSelector = '.js-flooper-item'] - Flooper children loopable items
* @param {number} [options.bufferSize = 10] - amount of pixels after block as past left side
* @param {number} [options.speed = 1] - amount of pixels container element should move per call.
* @param {String} [options.name] = 'flooperInstance' - Prefix to build unique id
*
* @callback onFloop - When an element of a flooper is looped
* @param {HTMLElment} flooperItem
* @param {Number} CurrentIndex
*
* @callback onStart - described next section
* @callback onPause - described next section
* @callback onPlay - described next section
* @callback onSlowmotion - described next section
*/

let myFlooper4 = new flooper('.js-flooper4', {
  autoPlay: true,
  bufferSize: 10,
  speed: 1,
  onFloop: () => {}, //noop
  onStart: () => {}, //noop
  onPlay: () => {}, //noop
  onPause: () => {}, //noop
  onSlowmotion: () => {}, //noop
});
