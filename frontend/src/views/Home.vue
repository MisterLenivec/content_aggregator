<template>
  <div class="home">
    <h2 class="tech-title text-center">Most popular tech news sites</h2>
    <div class="home-wrapper">
      <aside class="home-aside"></aside>
      <div class="boards-list-wrapper">
        <div class="boards-container">
          <div v-for="board in listBoards" :key="board.id"
               class="card bg-transparent board">
            <div class="card-header bg-transparent">
              <h5 class="card-title">{{ board.site_name }}</h5>
              <p class="line-hidden board-description card-text text-secondary"
                 :title="board.description">
                {{ board.description }}
              </p>
            </div>
            <ul class="list-group list-group-flush">
              <li v-for="article in listArticles"
                  v-if="article.site_board === board.site_name"
                  :key="article.id" class="list-group-item bg-transparent article">
                <a class="article-url" :href="article.url" target="_blank"
                   :title="article.title + '\n\n' + article.description">
                  <div class="img-container">
                    <img class="img-fluid article-img"
                         :src="article.image_url || board.image_url" alt="">
                  </div>
                  <span class="line-hidden article-title">
                    {{ article.title }}
                  </span>
                </a>
              </li>
            </ul>
            <div class="card-footer bg-transparent">
              <a :href="board.url" class="card-link" target="_blank">
                <span>{{ board.url }}</span>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="home-sidebar"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      listArticles: [],
      listBoards: [],
    }
  },
  components: {},
  created() {
    this.loadListArticles()
    this.loadListBoards()
  },
  methods: {
    async loadListArticles() {
      this.listArticles = await fetch(
          `${this.$store.getters.getServerUrl}/article`
      ).then(response => response.json())
      console.log(this.listArticles)
    },
    async loadListBoards() {
      this.listBoards = await fetch(
          `${this.$store.getters.getServerUrl}/board`
      ).then(response => response.json())
      console.log(this.listBoards)
    }
  }
};
</script>

<style scoped>
.home-wrapper {
  width: 100%;
  display: -ms-grid;
  display: grid;
  -ms-grid-columns: auto minmax(auto, 1200px) auto;
  grid-template-columns: auto minmax(auto, 1200px) auto;
  -ms-grid-rows: 5px auto 5px;
  grid-template-rows: auto;
      grid-template-areas:
      "aside main sidebar";
  grid-row-gap: 5px;
}
.home-aside {
  -ms-grid-row: 2;
  -ms-grid-column: 1;
  grid-area: aside;
  background-color: #ffffff;
}
.boards-list-wrapper {
  -ms-grid-row: 2;
  -ms-grid-column: 3;
  grid-area: main;
  background-color: #ffffff;
  /*background-color: #e8e2fb;*/
}
.home-sidebar {
  -ms-grid-row: 2;
  -ms-grid-column: 5;
  grid-area: sidebar;
  background-color: #ffffff;
}
.boards-list-wrapper {
  display: -ms-grid;
  display: grid;
  grid-template-columns: 1fr repeat(12, minmax(auto, 100px)) 1fr;
  padding: 15px 0;
}
.boards-container {
  -ms-grid-column: 2;
  -ms-grid-column-span: 12;
  grid-column: 2 / span 12;
  display: -ms-grid;
  display: grid;
  grid-template-columns: repeat(12, minmax(auto, 95px));
  grid-gap: 6px;
}
.board {
  -ms-grid-column-span: 4;
  grid-column-end: span 4;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  border-radius: .3rem;
}
.tech-title {
  font-weight: bold;
  padding: 5px;
  margin: 0;
  background: #e8e2fb;
}
.board-description {
  height: 48px;
}
.card, .list-group-item, .card-header {
  border-color: #ffddba;
}
.card-title {
  color: #d1925d;
  cursor: default;
}
.card-link {
  color: #d1925d;
}
.card-link:hover, .article-url:hover {
  color: #5f9ea0;
}
.article {
  height: 309px;
  text-align: center;
}
.article-title {
  padding-top: 7px;
}
.img-container {
  height: 236px;
}
.article-img {
  max-height: 236px;
}
.article-url {
  text-decoration: none;
  color: #212529;
  text-align: center;
}
.line-hidden {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow-y: hidden;
  text-overflow: ellipsis;
  text-align: left;
}

@media all and (max-width: 1200px) {
  .boards-container {
    -ms-grid-column: 2;
    -ms-grid-column-span: 8;
    grid-column: 4 / span 8;
    grid-template-columns: repeat(8, minmax(auto, 95px));
    grid-gap: 6px;
  }
  .board {
    -ms-grid-column-span: 4;
    grid-column-end: span 4;
  }
}
@media all and (max-width: 850px) {
  .board {
    -ms-grid-column-span: 12;
    grid-column-end: span 12;
  }
  .tech-title {
    font-size: 22px;
  }
}
</style>
