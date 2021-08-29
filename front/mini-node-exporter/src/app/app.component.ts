import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {MetricsApiService} from './metrics/metrics-api.service';
import {Metrics} from './metrics/metrics.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent implements OnInit, OnDestroy  {
  title = 'mini-node-exporter';
  metricsListSubs: Subscription = new Subscription;
  host: Metrics[] = [];
  uptime: Metrics[] = [];
  loadavg: Metrics[] = [];
  pro: Metrics[] = [];
  constructor(private metricsApi: MetricsApiService) {
  }

  ngOnInit() {
    this.metricsListSubs = this.metricsApi.getHost().subscribe(res => {
        console.log(res);  
        this.host = res;
        return this.host
          
        },
        console.error);

        this.metricsListSubs = this.metricsApi.getUptime().subscribe(res => {
          console.log(res);  
          this.uptime = res;
          return this.uptime
            
          },
          console.error);

          this.metricsListSubs = this.metricsApi.getLoad().subscribe(res => {
            console.log(res);  
            this.loadavg = res;
            return this.loadavg
              
            },
            console.error);


  }

  ngOnDestroy() {
    this.metricsListSubs.unsubscribe();
  }
}

