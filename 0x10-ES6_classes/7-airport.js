export default class Airport {
    constructor(name, code) {
      if (typeof name === 'string' && typeof code === 'string') {
        this._name = name;
        this._code = code;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    toString() {
      return `[object ${this._code}]`;
    }
  }
