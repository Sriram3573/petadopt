const blogPosts = document.querySelectorAll(".blog-post");

blogPosts.forEach(post => {
  post.addEventListener("click", () => {
    const title = post.querySelector("h3").textContent;
    alert(`You clicked on: ${title}. Full post coming soon!`);
  });
});
