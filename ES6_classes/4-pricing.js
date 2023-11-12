import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw TypeError('Amount must be a number');
    }

    if (!(currency instanceof Currency)) {
      throw TypeError('Currency must be a Currency');
    }

    this._amount = amount;
    this._currency = currency;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      throw TypeError('Amount must be a number');
    }

    this._amount = value;
  }

  get amount() {
    return this._amount;
  }

  set currency(value) {
    if (!(currency instanceof Currency)) {
      throw TypeError('Currency must be a Currency');
    }

    this._currency = value;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw TypeError('Amount must be a number');
    }

    if (typeof conversionRate !== 'number') {
      throw TypeError('ConversionRate must be a number');
    }

    return amount * conversionRate;
  }
}
