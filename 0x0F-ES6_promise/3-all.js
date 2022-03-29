import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then((obj) => console.log(`${obj[0].body} ${obj[1].firstName} ${obj[1].lastName}`)).catch(() => console.log('Signup system offline'));
}
