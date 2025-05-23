/**
 * The Selling Partner API for FBA inbound operations.
 * The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.
 *
 * The version of the OpenAPI document: 2024-03-20
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'
import { Pagination } from './Pagination.js'
import { SelfShipAppointmentSlotsAvailability } from './SelfShipAppointmentSlotsAvailability.js'

/**
 * The GetSelfShipAppointmentSlotsResponse model module.
 * @module fulfillmentinbound_v2024_03_20/model/GetSelfShipAppointmentSlotsResponse
 * @version 2024-03-20
 */
export class GetSelfShipAppointmentSlotsResponse {
  /**
   * Constructs a new <code>GetSelfShipAppointmentSlotsResponse</code>.
   * The &#x60;getSelfShipAppointmentSlots&#x60; response.
   * @alias module:fulfillmentinbound_v2024_03_20/model/GetSelfShipAppointmentSlotsResponse
   * @class
   * @param selfShipAppointmentSlotsAvailability {module:fulfillmentinbound_v2024_03_20/model/SelfShipAppointmentSlotsAvailability}
   */
  constructor (selfShipAppointmentSlotsAvailability) {
    this.selfShipAppointmentSlotsAvailability = selfShipAppointmentSlotsAvailability
  }

  /**
   * Constructs a <code>GetSelfShipAppointmentSlotsResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:fulfillmentinbound_v2024_03_20/model/GetSelfShipAppointmentSlotsResponse} obj Optional instance to populate.
   * @return {module:fulfillmentinbound_v2024_03_20/model/GetSelfShipAppointmentSlotsResponse} The populated <code>GetSelfShipAppointmentSlotsResponse</code> instance.
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
      obj = obj || new GetSelfShipAppointmentSlotsResponse()
      if (data.hasOwnProperty('pagination')) { obj.pagination = Pagination.constructFromObject(data.pagination) }
      if (data.hasOwnProperty('selfShipAppointmentSlotsAvailability')) { obj.selfShipAppointmentSlotsAvailability = SelfShipAppointmentSlotsAvailability.constructFromObject(data.selfShipAppointmentSlotsAvailability) }
    }
    return obj
  }
}

/**
 * @member {module:fulfillmentinbound_v2024_03_20/model/Pagination} pagination
 */
GetSelfShipAppointmentSlotsResponse.prototype.pagination = undefined

/**
 * @member {module:fulfillmentinbound_v2024_03_20/model/SelfShipAppointmentSlotsAvailability} selfShipAppointmentSlotsAvailability
 */
GetSelfShipAppointmentSlotsResponse.prototype.selfShipAppointmentSlotsAvailability = undefined
