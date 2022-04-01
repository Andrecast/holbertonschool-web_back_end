export default class HolbertonCourse {
    constructor(name, length, students) {
      this.constructor.verify(name, length, students);
      this._name = name;
      this._length = length;
      this._students = students;
    }
  
    static verify(name = null, length = null, students = null) {
      if (name !== null && typeof name !== 'string') {
        throw TypeError('Name must be a string');
      }
      if (length !== null && typeof length !== 'number') {
        throw TypeError('Length must be a string');
      }
      if (students !== null && !(Array.isArray(students))) {
        throw TypeError('Students must be an array of strings');
      }
      if (students !== null) {
        for (const x of students) {
          if (typeof x !== 'string') {
            throw TypeError('Students must be an array of strings');
          }
        }
      }
    }
  
    get name() {
      return this._name;
    }
  
    get length() {
      return this._length;
    }
  
    get students() {
      return this._students;
    }
  
    set name(name) {
      this.constructor.verify(name);
      this._name = name;
    }
  
    set length(length) {
      this.constructor.verify(null, length);
      this._length = length;
    }
  
    set students(students) {
      this.constructor.verify(null, null, students);
      this._students = students;
    }
  }
