/**
 * Selling Partner API for Replenishment
 * The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.  The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.
 *
 * The version of the OpenAPI document: 2022-11-07
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'

/**
 * The TimeInterval model module.
 * @module replenishment_v2022_11_07/model/TimeInterval
 * @version 2022-11-07
 */
export class TimeInterval {
  /**
   * Constructs a new <code>TimeInterval</code>.
   * A date-time interval in ISO 8601 format which is used to compute metrics. Only the date is required, but you must pass the complete date and time value. For example, November 11, 2022 should be passed as \&quot;2022-11-07T00:00:00Z\&quot;. Note that only data for the trailing 2 years is supported.   **Note**: The &#x60;listOfferMetrics&#x60; operation only supports a time interval which covers a single unit of the aggregation frequency. For example, for a MONTH aggregation frequency, the duration of the interval between the startDate and endDate can not be more than 1 month.
   * @alias module:replenishment_v2022_11_07/model/TimeInterval
   * @class
   * @param startDate {Date} When this object is used as a request parameter, the specified `startDate` is adjusted based on the aggregation frequency.  * For `WEEK` the metric is computed from the first day of the week (Sunday, based on ISO 8601) that contains the `startDate`. * For `MONTH` the metric is computed from the first day of the month that contains the `startDate`. * For `QUARTER` the metric is computed from the first day of the quarter that contains the `startDate`. * For `YEAR` the metric is computed from the first day of the year that contains the `startDate`.
   * @param endDate {Date} When this object is used as a request parameter, the specified `endDate` is adjusted based on the aggregation frequency.  * For `WEEK` the metric is computed up to the last day of the week (Sunday, based on ISO 8601) that contains the `endDate`. * For `MONTH`, the metric is computed up to the last day that contains the `endDate`. * For `QUARTER` the metric is computed up to the last day of the quarter that contains the `endDate`. * For `YEAR` the metric is computed up to the last day of the year that contains the `endDate`.  Note: The end date may be adjusted to a lower value based on the data available in our system.
   */
  constructor (startDate, endDate) {
    this.startDate = startDate
    this.endDate = endDate
  }

  /**
   * Constructs a <code>TimeInterval</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:replenishment_v2022_11_07/model/TimeInterval} obj Optional instance to populate.
   * @return {module:replenishment_v2022_11_07/model/TimeInterval} The populated <code>TimeInterval</code> instance.
   */
  static constructFromObject (data, obj) {
    if (data) {
      switch (typeof data) {
        case 'string':
          obj = String(data)
          break
        case 'number':
          obj = Number(data)
          break
        case 'boolean':
          obj = Boolean(data)
          break
      }
      obj = obj || new TimeInterval()
      if (data.hasOwnProperty('startDate')) { obj.startDate = ApiClient.convertToType(data.startDate, 'Date') }
      if (data.hasOwnProperty('endDate')) { obj.endDate = ApiClient.convertToType(data.endDate, 'Date') }
    }
    return obj
  }
}

/**
 * When this object is used as a request parameter, the specified `startDate` is adjusted based on the aggregation frequency.  * For `WEEK` the metric is computed from the first day of the week (Sunday, based on ISO 8601) that contains the `startDate`. * For `MONTH` the metric is computed from the first day of the month that contains the `startDate`. * For `QUARTER` the metric is computed from the first day of the quarter that contains the `startDate`. * For `YEAR` the metric is computed from the first day of the year that contains the `startDate`.
 * @member {Date} startDate
 */
TimeInterval.prototype.startDate = undefined

/**
 * When this object is used as a request parameter, the specified `endDate` is adjusted based on the aggregation frequency.  * For `WEEK` the metric is computed up to the last day of the week (Sunday, based on ISO 8601) that contains the `endDate`. * For `MONTH`, the metric is computed up to the last day that contains the `endDate`. * For `QUARTER` the metric is computed up to the last day of the quarter that contains the `endDate`. * For `YEAR` the metric is computed up to the last day of the year that contains the `endDate`.  Note: The end date may be adjusted to a lower value based on the data available in our system.
 * @member {Date} endDate
 */
TimeInterval.prototype.endDate = undefined
