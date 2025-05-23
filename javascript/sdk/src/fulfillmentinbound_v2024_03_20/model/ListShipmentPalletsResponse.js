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
import { Pallet } from './Pallet.js'

/**
 * The ListShipmentPalletsResponse model module.
 * @module fulfillmentinbound_v2024_03_20/model/ListShipmentPalletsResponse
 * @version 2024-03-20
 */
export class ListShipmentPalletsResponse {
  /**
   * Constructs a new <code>ListShipmentPalletsResponse</code>.
   * The &#x60;listShipmentPallets&#x60; response.
   * @alias module:fulfillmentinbound_v2024_03_20/model/ListShipmentPalletsResponse
   * @class
   * @param pallets {Array.<module:fulfillmentinbound_v2024_03_20/model/Pallet>} The pallets in a shipment.
   */
  constructor (pallets) {
    this.pallets = pallets
  }

  /**
   * Constructs a <code>ListShipmentPalletsResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:fulfillmentinbound_v2024_03_20/model/ListShipmentPalletsResponse} obj Optional instance to populate.
   * @return {module:fulfillmentinbound_v2024_03_20/model/ListShipmentPalletsResponse} The populated <code>ListShipmentPalletsResponse</code> instance.
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
      obj = obj || new ListShipmentPalletsResponse()
      if (data.hasOwnProperty('pagination')) { obj.pagination = Pagination.constructFromObject(data.pagination) }
      if (data.hasOwnProperty('pallets')) { obj.pallets = ApiClient.convertToType(data.pallets, [Pallet]) }
    }
    return obj
  }
}

/**
 * @member {module:fulfillmentinbound_v2024_03_20/model/Pagination} pagination
 */
ListShipmentPalletsResponse.prototype.pagination = undefined

/**
 * The pallets in a shipment.
 * @member {Array.<module:fulfillmentinbound_v2024_03_20/model/Pallet>} pallets
 */
ListShipmentPalletsResponse.prototype.pallets = undefined
