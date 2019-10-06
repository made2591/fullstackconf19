<template>
  <div>
    <md-table v-model="users" :table-header-color="tableHeaderColor">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Family">{{ item.family }}</md-table-cell>
        <md-table-cell md-label="Cost">{{ item.cost }}</md-table-cell>
        <md-table-cell md-label="Actions">{{ item.actions }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
export default {
  name: "ordered-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      selected: [],
      users: [
        {
          id: "i-0009ace46faa3dd1e",
          family: "t3.small",
          cost: "$4,342",
          actions: "Oud-Turnhout"
        },
        {
          id: "i-00114f400ed271d12",
          family: "t3.small",
          cost: "$4,342",
          actions: "Oud-Turnhout"
        },
        {
          id: "i-00144861ba4a87f84",
          family: "t3.small",
          cost: "$4,342",
          actions: "Oud-Turnhout"
        },
        {
          id: "i-002079b2d1cb3b6a1",
          family: "t3.small",
          cost: "$4,342",
          actions: "Oud-Turnhout"
        },
        {
          id: "i-0035e4a725ffdc125",
          family: "t3.small",
          cost: "$4,342",
          actions: "Oud-Turnhout"
        },
        {
          id: "i-0046e4f725eecc142",
          family: "t3.small",
          cost: "$4,342",
          actions: "Oud-Turnhout"
        }
      ]
    };
  }
};
</script>
