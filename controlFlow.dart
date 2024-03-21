import 'dart:io';

void main() {
  // print("Enter a number: "); accepts input in a new line
  // String? number = stdin.readLineSync(); how to read string input
  stdout.write("Enter a number: ");
  int? number = int.parse(stdin.readLineSync()!);
  if( number > 10) {
    print("Your number is greater than $number");
  }
  else if (number < 10) {
    print("Your number is less than $number");
  }
  else {
    print("Your number is equal to 10");
  }
}
