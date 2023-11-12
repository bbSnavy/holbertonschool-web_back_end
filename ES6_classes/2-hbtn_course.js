export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }

    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }

    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array');
    }

    students.forEach((value) => {
      if (typeof value !== 'string') {
        throw TypeError('Student must be a string');
      }
    });

    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw TypeError('Name must be a string');
    }

    this._name = value;
  }

  get name() {
    return this._name;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw TypeError('Length must be a number');
    }

    this._length = value;
  }

  get length() {
    return this._length;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw TypeError('Students must be an array of strings');
    }

    value.forEach((v) => {
      if (typeof v !== 'string') {
        throw TypeError('Students must be an array of strings');
      }
    });

    this._students = value;
  }

  get students() {
    return this._students;
  }
}
