document.addEventListener('DOMContentLoaded', function() {
    loadArticles('geo_news', 1);
});

function loadArticles(channel, page) {
    fetch(`/api/articles/${channel}?page=${page}`)
        .then(response => response.json())
        .then(data => {
            const articlesContainer = document.getElementById('articles');
            articlesContainer.innerHTML = '';

            data.articles.forEach(article => {
                const articleElement = document.createElement('div');
                articleElement.classList.add('col-md-4', 'mb-4');

                articleElement.innerHTML = `
                    <div class="card h-100">
                        <img src="${article.image}" class="card-img-top" alt="${article.title}">
                        <div class="card-body">
                            <h5 class="card-title">${article.title}</h5>
                            <p class="card-text">${article.date}</p>
                            <a href="${article.link}" target="_blank" class="btn btn-primary">Read more</a>
                        </div>
                    </div>
                `;

                articlesContainer.appendChild(articleElement);
            });

            const paginationContainer = document.getElementById('pagination');
            paginationContainer.innerHTML = '';

            const totalPages = Math.ceil(data.total_articles / data.per_page);

            if (page > 1) {
                const prevPage = document.createElement('li');
                prevPage.classList.add('page-item');
                prevPage.innerHTML = `<a class="page-link" href="#" onclick="loadArticles('${channel}', ${page - 1})">Previous</a>`;
                paginationContainer.appendChild(prevPage);
            }

            for (let i = 1; i <= totalPages; i++) {
                const pageItem = document.createElement('li');
                pageItem.classList.add('page-item', i === page ? 'active' : '');
                pageItem.innerHTML = `<a class="page-link" href="#" onclick="loadArticles('${channel}', ${i})">${i}</a>`;
                paginationContainer.appendChild(pageItem);
            }

            if (page < totalPages) {
                const nextPage = document.createElement('li');
                nextPage.classList.add('page-item');
                nextPage.innerHTML = `<a class="page-link" href="#" onclick="loadArticles('${channel}', ${page + 1})">Next</a>`;
                paginationContainer.appendChild(nextPage);
            }
        })
        .catch(error => console.error('Error fetching articles:', error));
}