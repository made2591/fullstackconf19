<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-50">
        <chart-card
          :chart-data="dailySalesChart.data"
          :chart-options="dailySalesChart.options"
          :chart-type="'Line'"
          data-background-color="blue"
        >
          <template slot="content">
            <h4 class="title">Billed Hours per Day</h4>
            <p class="category">
              <span class="text-success">
                <i class="fas fa-long-arrow-alt-up"></i> 55%
              </span>
              increase in today usage.
            </p>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>access_time</md-icon>updated 4 minutes ago
            </div>
          </template>
        </chart-card>
      </div>
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-50">
        <chart-card
          :chart-data="emailsSubscriptionChart.data"
          :chart-options="emailsSubscriptionChart.options"
          :chart-responsive-options="emailsSubscriptionChart.responsiveOptions"
          :chart-type="'Bar'"
          data-background-color="red"
        >
          <template slot="content">
            <h4 class="title">Average Boot Time (sec) per Day</h4>
            <p class="category">Last Week Performance</p>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>access_time</md-icon>updated 3 minutes ago
            </div>
          </template>
        </chart-card>
      </div>
      <!-- <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-33">
        <chart-card
          :chart-data="dataCompletedTasksChart.data"
          :chart-options="dataCompletedTasksChart.options"
          :chart-type="'Line'"
          data-background-color="green"
        >
          <template slot="content">
            <h4 class="title">Completed Tasks</h4>
            <p class="category">Last Campaign Performance</p>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>access_time</md-icon>campaign sent 26 minutes ago
            </div>
          </template>
        </chart-card>
      </div>-->
      <div class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-33">
        <stats-card data-background-color="brown">
          <template slot="header">
            <md-icon>monetization_on</md-icon>
          </template>

          <template slot="content">
            <p class="category">Daily Bill</p>
            <h3 class="title">$6,24</h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>date_range</md-icon>Last 24 Hours
            </div>
          </template>
        </stats-card>
      </div>
      <div class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-33">
        <stats-card data-background-color="purple">
          <template slot="header">
            <md-icon>file_copy</md-icon>
          </template>

          <template slot="content">
            <p class="category">Global User Space</p>
            <h3 class="title">
              23/500
              <small>GB</small>
            </h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>info</md-icon>
              <a href="#">Get More Space...</a>
            </div>
          </template>
        </stats-card>
      </div>
      <div class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-33">
        <stats-card data-background-color="grey">
          <template slot="header">
            <md-icon>supervised_user_circle</md-icon>
          </template>

          <template slot="content">
            <p class="category">Connected Users</p>
            <h3 class="title">4</h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>date_range</md-icon>Updated 3 minutes ago
            </div>
          </template>
        </stats-card>
      </div>
      <!-- <div class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-25">
        <stats-card data-background-color="blue">
          <template slot="header">
            <i class="fab fa-twitter"></i>
          </template>

          <template slot="content">
            <p class="category">Folowers</p>
            <h3 class="title">+245</h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>update</md-icon>Just Updated
            </div>
          </template>
        </stats-card>
      </div>-->
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-60">
        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Your Environments</h4>
          </md-card-header>
          <md-card-content>
            <ordered-table table-header-color="green"></ordered-table>
          </md-card-content>
        </md-card>
      </div>
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-40">
        <!-- <nav-tabs-card>
          <template slot="content">
            <span class="md-nav-tabs-title">Tasks:</span>
            <md-tabs class="md-success" md-alignment="left">
              <md-tab id="tab-home" md-label="Bugs" md-icon="bug_report">
                <nav-tabs-table></nav-tabs-table>
              </md-tab>

              <md-tab id="tab-pages" md-label="Website" md-icon="code">
                <nav-tabs-table></nav-tabs-table>
              </md-tab>

              <md-tab id="tab-posts" md-label="server" md-icon="cloud">
                <nav-tabs-table></nav-tabs-table>
              </md-tab>
            </md-tabs>
          </template>
        </nav-tabs-card>-->
        <form>
          <md-card>
            <md-card-header data-background-color="orange">
              <h4 class="title">Create New Environment</h4>
            </md-card-header>

            <md-card-content>
              <div class="md-layout">
                <div class="md-layout-item md-small-size-100 md-size-100">
                  <md-field>
                    <label>Instance Family</label>
                    <md-select name="movie" id="movie">
                      <md-optgroup label="Shared Hardware">
                        <md-option value="t3.medium">2 vcpu, 4GB ram</md-option>
                        <md-option value="c5.xlarge">4 vcpu, 8GB ram</md-option>
                        <md-option value="m5.4xlarge">16 vcpu, 64GB ram</md-option>
                        <md-option value="x1.32xlarge">Take my money (128 vcpu, 2TB Ram)</md-option>
                      </md-optgroup>

                      <md-optgroup label="Compute Optimized">
                        <md-option value="t3.medium">2 vcpu, 4GB ram</md-option>
                        <md-option value="c5.xlarge">4 vcpu, 8GB ram</md-option>
                        <md-option value="m5.4xlarge">16 vcpu, 64GB ram</md-option>
                        <md-option value="x1.32xlarge">Take my money (128 vcpu, 2TB Ram)</md-option>
                      </md-optgroup>

                      <md-optgroup label="Network Optimized">
                        <md-option value="t3.medium">2 vcpu, 4GB ram</md-option>
                        <md-option value="c5.xlarge">4 vcpu, 8GB ram</md-option>
                        <md-option value="m5.4xlarge">16 vcpu, 64GB ram</md-option>
                        <md-option value="x1.32xlarge">Take my money (128 vcpu, 2TB Ram)</md-option>
                      </md-optgroup>
                    </md-select>
                  </md-field>
                </div>
                <div class="md-layout-item md-small-size-100 md-size-100">
                  <md-field>
                    <label>Workspace (Optional)</label>
                    <md-select name="movie" id="movie" md-dense>
                      <md-option
                        value="vol-0a748d95c291a9859"
                        selected="selected"
                      >vol-0a748d95c291a9859</md-option>
                      <md-option value="vol-0a748d95c291a9859">vol-0a748d95c291a9859</md-option>
                      <md-option value="vol-0a748d95c291a9859">vol-0a748d95c291a9859</md-option>
                      <md-option value="vol-0a748d95c291a9859">vol-0a748d95c291a9859</md-option>
                    </md-select>
                  </md-field>
                </div>
                <div class="md-layout-item md-small-size-100 md-size-100">
                  <md-field>
                    <label>Disk Size in GB (Optional)</label>
                    <md-input type="number" value="30"></md-input>
                  </md-field>
                </div>
                <div class="md-layout-item md-size-100 text-right">
                  <md-button class="md-raised md-warning">Create</md-button>
                </div>
              </div>
            </md-card-content>
          </md-card>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {
  StatsCard,
  ChartCard,
  // NavTabsCard,
  // NavTabsTable,
  OrderedTable
} from "@/components";

export default {
  components: {
    StatsCard,
    ChartCard,
    // NavTabsCard,
    // NavTabsTable,
    OrderedTable
  },
  data() {
    return {
      dailySalesChart: {
        data: {
          labels: ["M", "T", "W", "T", "F", "S", "S"],
          series: [[12, 17, 7, 17, 23, 18, 38]]
        },
        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      dataCompletedTasksChart: {
        data: {
          // labels: ["12am", "3pm", "6pm", "9pm", "12pm", "3am", "6am", "9am"],
          // series: [[230, 750, 450, 300, 280, 240, 200, 190]]
          labels: ["M", "T", "W", "T", "F", "S", "S"],
          series: [[230, 750, 450, 300, 280, 240, 200]]
        },

        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      emailsSubscriptionChart: {
        data: {
          // labels: [
          //   "Ja",
          //   "Fe",
          //   "Ma",
          //   "Ap",
          //   "Mai",
          //   "Ju",
          //   "Jul",
          //   "Au",
          //   "Se",
          //   "Oc",
          //   "No",
          //   "De"
          // ],
          labels: ["M", "T", "W", "T", "F", "S", "S"],
          //series: [[542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]]
          series: [[342, 243, 120, 480, 353, 253, 126]]
        },
        options: {
          axisX: {
            showGrid: false
          },
          low: 0,
          high: 800,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0
          }
        },
        responsiveOptions: [
          [
            "screen and (max-width: 640px)",
            {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function(value) {
                  return value[0];
                }
              }
            }
          ]
        ]
      }
    };
  }
};
</script>
