export default function signUpUser(firstName, lastName) {
  const user = { firstName, lastName };
  return Promise.resolve(user);
}
