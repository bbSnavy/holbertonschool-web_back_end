export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw TypeError('sqft must be a number');
    }

    this._sqft = sqft;

    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  set sqft(value) {
    if (typeof sqft !== 'number') {
      throw TypeError('sqft must be a number');
    }

    this._sqft = value;
  }

  get sqft() {
    return this._sqft;
  }
}
