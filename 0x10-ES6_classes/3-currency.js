export default class Currency {
    constructor(code, name) {
      if (typeof code === 'string' && typeof name === 'string') {
        this._code = code;
        this._name = name;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    get name() {
      return this._name;
    }
  
    get code() {
      return this._code;
    }
  
    set name(name) {
      if (typeof name === 'string') {
        this._name = name;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    set code(code) {
      if (typeof code === 'string') {
        this._code = code;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
  }
