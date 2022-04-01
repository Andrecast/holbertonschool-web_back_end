export default class HolbertonClass {
    constructor(size, location) {
      if (typeof size === 'number' && typeof location === 'string') {
        this._size = size;
        this._location = location;
      } else {
        throw (TypeError('wrong data type'));
      }
    }
  
    [Symbol.toPrimitive](hint) {
      return hint === 'string' ? this._location : this._size;
    }
  }
