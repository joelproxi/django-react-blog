import axios from 'axios';

export async function getPosts() {
  try {
    const resp = await axios.get('http://127.0.0.1:8000/api/v1/blog/posts/');
    if (resp.status === 200) {
      const data = await resp.data;
      return data;
    }
  } catch (error) {
    console.error(error?.message);
  }
}

export async function getPost() {
  try {
    const resp = await axios.get(`http://127.0.0.1:8000/api/v1/blog/posts/${id}/`);
    if (resp.status === 200) {
      const data = await resp.data;
      return data;
    }
  } catch (error) {
    console.error(error?.message);
  }
}
