# This installs the version 2.1.0 flask package using pip3

package  {  'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
