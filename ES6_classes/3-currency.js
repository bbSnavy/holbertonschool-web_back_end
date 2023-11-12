export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    }

    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }

    this._code = code;
    this._name = name;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw TypeError('Code must be a string');
    }

    this._code = value;
  }

  get code() {
    return this._code;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw TypeError('Name must be a string');
    }

    this._name = value;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
