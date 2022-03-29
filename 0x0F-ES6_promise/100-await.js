import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photoval;
  let userval;
  try {
    photoval = await uploadPhoto();
    userval = await createUser();
  } catch (e) {
    photoval = null;
    userval = null;
  }
  return { photo: photoval, user: userval };
}
