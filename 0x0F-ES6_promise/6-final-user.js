import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return [{ status: 'fulfilled', value: await signUpUser(firstName, lastName).then((data) => data) }, { status: 'rejected', value: await uploadPhoto(fileName).catch((error) => error.toString()) }];
}
