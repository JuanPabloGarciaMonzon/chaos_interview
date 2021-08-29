import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable } from 'rxjs';
import {API_URL} from './env';
import {Metrics} from './metrics.model';

@Injectable()
export class MetricsApiService {

  constructor(private http: HttpClient) {
  }

  // GET list of public, future events
  getHost(): Observable<Metrics[]> {
    return <Observable<Metrics[]>> this.http
      .get(`${API_URL}/info/host`);
     
  }

    // GET list of public, future events
    getUptime(): Observable<Metrics[]> {
      return <Observable<Metrics[]>> this.http
        .get(`${API_URL}/info/uptime`);
             
    }

  // GET list of public, future events
  getLoad(): Observable<Metrics[]> {
    return <Observable<Metrics[]>> this.http
      .get(`${API_URL}/info/load`);      
  }



}