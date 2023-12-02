import {getPosts} from './postApi';

export async function postLoader() {
  const posts = await getPosts();
  return {posts};
}

export async function postDetailLoader() {
  const post = await getPosts();
  return {post};
}
