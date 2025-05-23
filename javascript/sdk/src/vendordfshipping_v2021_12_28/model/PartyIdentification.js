/**
 * Selling Partner API for Direct Fulfillment Shipping
 * Use the Selling Partner API for Direct Fulfillment Shipping to access a direct fulfillment vendor's shipping data.
 *
 * The version of the OpenAPI document: 2021-12-28
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'
import { Address } from './Address.js'
import { TaxRegistrationDetails } from './TaxRegistrationDetails.js'

/**
 * The PartyIdentification model module.
 * @module vendordfshipping_v2021_12_28/model/PartyIdentification
 * @version 2021-12-28
 */
export class PartyIdentification {
  /**
   * Constructs a new <code>PartyIdentification</code>.
   * The name, address, and tax details of a party.
   * @alias module:vendordfshipping_v2021_12_28/model/PartyIdentification
   * @class
   * @param partyId {String} The identifier of the party.
   */
  constructor (partyId) {
    this.partyId = partyId
  }

  /**
   * Constructs a <code>PartyIdentification</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:vendordfshipping_v2021_12_28/model/PartyIdentification} obj Optional instance to populate.
   * @return {module:vendordfshipping_v2021_12_28/model/PartyIdentification} The populated <code>PartyIdentification</code> instance.
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
      obj = obj || new PartyIdentification()
      if (data.hasOwnProperty('partyId')) { obj.partyId = ApiClient.convertToType(data.partyId, 'String') }
      if (data.hasOwnProperty('address')) { obj.address = Address.constructFromObject(data.address) }
      if (data.hasOwnProperty('taxRegistrationDetails')) { obj.taxRegistrationDetails = ApiClient.convertToType(data.taxRegistrationDetails, [TaxRegistrationDetails]) }
    }
    return obj
  }
}

/**
 * The identifier of the party.
 * @member {String} partyId
 */
PartyIdentification.prototype.partyId = undefined

/**
 * @member {module:vendordfshipping_v2021_12_28/model/Address} address
 */
PartyIdentification.prototype.address = undefined

/**
 * The tax registration details of the party.
 * @member {Array.<module:vendordfshipping_v2021_12_28/model/TaxRegistrationDetails>} taxRegistrationDetails
 */
PartyIdentification.prototype.taxRegistrationDetails = undefined
