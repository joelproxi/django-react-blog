import React from 'react';
import {useLoaderData} from 'react-router-dom';

const PostPage = () => {
  const {posts} = useLoaderData();
  console.log(posts);

  return <div></div>;
};

export default PostPage;
